// const fetch(`${import.meta.url}`)

// console.log(`${import.meta.url.replace(/[^\/]*$/, 'index.html')}`);

import {fetch_shadow} from '../util.js';


const content = fetch(import.meta.url.replace(/[^\/]*$/, 'index.html')).then((t)=>{
    return t.text();
}).then((t)=>{
  return new DOMParser().parseFromString(t, 'text/html');
}).catch((e)=>{
  console.log(e);
});

console.log(content);

export class MyRootComponent extends HTMLElement {
  constructor() {
    super();
    fetch_shadow(this, import.meta.url, '');
    // this.shadow = this.attachShadow({mode: 'open'});
    // content.then((c)=>{
    //   this.shadow.appendChild(c.getElementById('main').content.cloneNode(true));
    // }).catch(e=>{console.log(e)});
  }
}
