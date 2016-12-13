var gulp = require('gulp');
var compass = require('gulp-compass');
var minifyCSS = require('gulp-minify-css');

gulp.task('compass', function() {
    gulp.src('./css/sassaparilla/assets/css/*.scss')
        .pipe(compass({
            config_file: './css/sassaparilla/compass/config.rb',
            sass: 'css/sassaparilla/assets/css',
            css: 'css/sassaparilla/assets/css',
        }))
        .on('error', function(err) {
            console.log(err)
        })
        .pipe(minifyCSS())
        .pipe(gulp.dest('./assets/css/'));
});

gulp.task('default', ['compass']);
