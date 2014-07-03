##
## This file is only needed for Compass/Sass integration. If you are not using
## Compass, you may safely ignore or delete this file.
##

# Default to production if environment is not set.
saved = environment
if (environment.nil?)
  environment = :production
else
  environment = saved
end

# Location of the theme's resources.
css_dir = "static/css"
sass_dir = "sass"
images_dir = "static/img"
generated_images_dir = images_dir + "/generated"
javascripts_dir = "static/js"

# Require any additional compass plugins installed on your system.
require 'rgbapng'
require 'toolkit'
require 'sass-globbing'

# You can select your preferred output style here (can be overridden via the command line):
# output_style = :expanded or :nested or :compact or :compressed
output_style = (environment == :production) ? :compressed : :nested

# To enable relative paths to assets via compass helper functions.
relative_assets = true

# To disable debugging comments that display the original location of your selectors.
line_comments = environment == :development

# Add the 'sass' directory itself as an import path to ease imports.
add_import_path 'sass'
