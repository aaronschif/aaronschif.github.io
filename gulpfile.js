var gulp = require('gulp');
var pug = require('gulp-pug');
var sass = require('gulp-sass');
var imagemin = require('gulp-imagemin');
var svg2png = require('gulp-svg2png');

gulp.task('sass', function () {
  return gulp.src('./src/*.sass')
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(gulp.dest('./public/'));
});

gulp.task('image', function () {
    return gulp.src('src/*.svg')
        .pipe(imagemin())
        .pipe(gulp.dest('public/'))
        .pipe(svg2png())
        .pipe(gulp.dest('public/'));
})

gulp.task('pug', function () {
  return gulp.src('src/*.pug')
  .pipe(pug({
    pretty: true,
  })).pipe(gulp.dest('public/'));
});

gulp.task('default', ['sass', 'pug', 'image']);
