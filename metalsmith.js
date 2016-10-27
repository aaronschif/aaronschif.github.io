#!/usr/bin/env node
var Metalsmith  = require('metalsmith');
var collections = require('metalsmith-collections');
var layouts     = require('metalsmith-layouts');
var markdown    = require('metalsmith-markdown');
var permalinks  = require('metalsmith-permalinks');
var pug = require('metalsmith-pug');
var sass = require('metalsmith-sass');
var more = require('metalsmith-more');


Metalsmith(__dirname)
  .metadata({
    sitename: "My Static Site & Blog",
    siteurl: "http://example.com/",
    description: "It's about saying »Hello« to the world.",
    generatorname: "Metalsmith",
    generatorurl: "http://metalsmith.io/"
  })
  .source('./src')
  .destination('./build')
  .clean(true)
  .use(collections({
    posts: {
        pattern: 'blog/*/*.md',
        sortBy: 'date',
        reverse: true,
    }
  }))
  .use(markdown())
  .use(more())
  .use(layouts({
    engine: 'pug',
    default: 'post.pug',
    directory: 'src/_templates',
    pattern: 'blog/*/*.html',
  }))
  .use(permalinks({
      relative: false
  }))
  .use(pug({locals: {require: require}, useMetadata:true}))
  .use(permalinks({
      relative: false
  }))
  .use(sass())
  .build(function(err) {      // build process
    if (err) throw err;       // error handling is required
  });
