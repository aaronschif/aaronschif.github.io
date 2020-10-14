export function fetch_shadow(el, from, template) {
  return fetch(from.replace(/[^\/]*$/, template)).then((t)=>{
      return t.text();
  }).then((dom_string)=>{
    let dom = new DOMParser().parseFromString(dom_string, 'text/html');
    let shadow = el.attachShadow({mode: 'open'});
    shadow.appendChild(dom.getElementById('main').content.cloneNode(true));
  }).catch((e)=>{
    console.log(e);
  });
}
