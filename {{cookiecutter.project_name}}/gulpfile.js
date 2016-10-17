var fs = require('fs');
var path = require('path');
var gulp = require('gulp');
var $ = require('gulp-load-plugins')();
var sequence = require('run-sequence');
var mainBowerFiles = require('main-bower-files');
var Eyeglass = require('eyeglass');
var buffer = require('vinyl-buffer');
var merge = require('merge-stream');
var argv = require('yargs').argv;
var del = require('del');

// Check for --production flag
var isProduction = !!(argv.production);

// Browsers to target when prefixing CSS.
var COMPATIBILITY = ['last 2 versions', 'ie >= 9', 'and_chr >= 2.3'];

// Directories
var PATHS = {
  sass: 'src/core/sass',
  css: 'src/core/static/css',
  bower: 'bower_components',
  libs: 'src/core/static/libs'
};

// File patterns
var FILES = {
  sass: PATHS.sass + '/**/*.scss',
  css: PATHS.css + '/**/*.css'
};

// Sass options
var SASS = {
  include: [
    PATHS.sass
    {%- if cookiecutter.foundation == 'yes' %},
    PATHS.bower + '/foundation-sites/scss'
    {%- endif %}
  ],
  assets: {
    httpPrefix: '/static',
    sources: [
      {directory: 'static', globOpts: {ignore: ['**/*js', '**/*.txt']}}
    ]
  }
};


/**
 * ---------
 * LIBRARIES
 * ---------
 */

// Bower install task
gulp.task('bower', function () {
  return $.bower()
    .pipe(gulp.dest(PATHS.bower));
});

// Only add main files from bower_components to git
gulp.task('copy:libs', ['clean:libs'], function () {
  return gulp.src(mainBowerFiles(), {base: PATHS.bower})
    .pipe(gulp.dest(PATHS.libs));
});


/**
 * ----
 * SASS
 * ----
 */

gulp.task('sass', argv.clean ? ['clean:css'] : [], function () {
  // Prepare eyglass options
  var eyeglass = new Eyeglass({
    includePaths: SASS.include,
    eyeglass: {assets: SASS.assets}
  });

  // Add a modification timestamp to assets as a query parameter
  eyeglass.assets.resolver(function (assetFile, assetUri, oldResolver, done) {
    var mtime = fs.statSync(assetFile).mtime.getTime();
    done(null, {
      path: assetUri,
      query: mtime.toString()
    });
  });

  return gulp.src(FILES.sass)
    // .pipe($.sourcemaps.init())
    // compile css
    .pipe($.sass(eyeglass.options)
      .on('error', $.sass.logError))
    // add vendor prefixes
    .pipe($.autoprefixer({
      browsers: COMPATIBILITY
    }))
    // optimize
    .pipe($.if(isProduction, $.cssnano()))
    // add sourcemaps
    // .pipe($.if(!isProduction, $.sourcemaps.write()))
    .pipe(gulp.dest(PATHS.css));
});


/**
 * --------------
 * CLEANING TASKS
 * --------------
 */

gulp.task('clean', ['clean:libs', 'clean:css']);

gulp.task('clean:libs', function () {
  return del([PATHS.libs]);
});

gulp.task('clean:css', function () {
  return del([PATHS.css]);
});


/**
 * -------------
 * DEFAULT TASKS
 * -------------
 */

gulp.task('build', function (done) {
  sequence(['clean', 'copy:libs', 'sass'], done);
});

gulp.task('watch', function () {
  gulp.watch(mainBowerFiles(), ['copy:libs']);
  gulp.watch(FILES.sass, ['sass']);
});

gulp.task('default', function (done) {
  sequence(['build', 'watch'], done);
});
