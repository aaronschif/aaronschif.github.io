import {fetch_shadow} from '../util.js';


export class MyResume extends HTMLElement  {
  constructor() {
    super();
    fetch_shadow(this, import.meta.url, '');
  }
}
