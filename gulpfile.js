var gulp = require('gulp');
var pug = require('gulp-pug');
var sass = require('gulp-sass');
var imagemin = require('gulp-imagemin');
var svg2png = require('gulp-svg2png');
var through = require('through2')


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
        locals: {
            require: require
        },
      }))
      .pipe(gulp.dest('public/'));
});

// gulp.task('default', ['sass', 'pug', 'image']);

gulp.task('posts', ()=>{
    let thing = through.obj(function(chunk, enc, callback){
        console.log(chunk, enc, callback)
        console.log(chunk.path)
        this.push(chunk)
        callback()
    })

    return gulp.src('src/posts/*')
        .pipe(thing)
        .pipe(gulp.dest('public/posts/'));
})

// gulp.task('watch', ['default'], ()=>{
//     gulp.watch('src/**', ['default'])
// })
