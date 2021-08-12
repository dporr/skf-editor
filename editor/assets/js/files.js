let depth = 0;
async function indexFiles(){
const FILES_API = "http://0.0.0.0:1337/api/indexer/files";
const HEADERS = {};
const response = await fetch(FILES_API, HEADERS)
console.log("fetched")
const files = await response.json();
if(response.ok){
    parseFilesResponse(files['files'])
}
}

function createICNode(id, name, dir){
//console.log("ID", id)
//We are inheriting all this properties from IceCoder
let padding = depth;
let visible= depth>0 ? "block":"block"
let itemClass = dir? "pft-directory dirOpen": "pft-file ext-php"
let li = document.createElement('li')
let a = document.createElement('a')
li.setAttribute('class', `${itemClass}`)
li.setAttribute('id', id)
a.title = name
a.setAttribute("nohref", "")
a.setAttribute("ondragover", "parent.ICEcoder.overFileFolder('folder', '|'); parent.ICEcoder.highlightFileFolder('|', true);")
a.setAttribute("ondragleave", "parent.ICEcoder.overFileFolder('folder', ''); parent.ICEcoder.highlightFileFolder('|', false);") 
a.setAttribute("onmouseover", "parent.ICEcoder.overFileFolder('folder', '|')" )
a.setAttribute("onmouseout", "parent.ICEcoder.overFileFolder('folder', '')" )
a.setAttribute("onclick", "parent.ICEcoder.openCloseDir(this)" )
a.setAttribute("style", `position:relative; color:#eee; font-size:12px; cursor:pointer;left: ${padding}px; display=${visible}` )
a.setAttribute("class", `${itemClass}`)
a.textContent=name
li.appendChild(a)
return li;
}


function parseFilesResponse(jsonResponse, parent){   
//console.log(jsonResponse)
depth++;
let root = document.createElement('ul')
if(parent !== undefined){
    root = parent //document.getElementById(parent)
}
Object.keys(jsonResponse).forEach(function(key){
    node = jsonResponse[key];
   // console.log(node['name'], node['type']);
    if(node['type'] === 'dir' && node.child.length != 0){
        //folder = document.createElement('ul')
        root.appendChild(createICNode(
            key,
            "FOLDER: " + node['name'],
            true
        ))
        depth++;
        root =  document.createElement('ul')
        parseFilesResponse(node.child[0]['files'],root)
        depth = 0;
    }else{
        root.appendChild(createICNode(
            key,
            node['name']
        ))
    }
    document.body.appendChild(root)
    }
)
}