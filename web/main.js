import {MyRootComponent} from './components/main/main.js';
import {MyResume} from './components/resume/main.js';

customElements.define('my-root-component', MyRootComponent, {});
customElements.define('my-resume', MyResume, {});

export function init() {
  console.log('init');
}
