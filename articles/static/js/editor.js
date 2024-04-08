div = document.getElementsByClassName("block")[document.getElementsByClassName("block").length - 1];
function constructPacket(){
    let title = document.querySelector("#title").value;
    let published = document.querySelector("#published").checked;
    let blocks = [];
    let block_ind = 0;
    
    //Construct a JSON packet
    for (var block of document.querySelector("#content").children){
        blocks.push([]);
        let el_ind = 0;

        for (var el of block.children){
            blocks[block_ind].push({});
            blocks[block_ind][el_ind]["type"] = el.getAttribute("class");
            blocks[block_ind][el_ind]["content"] = el.value;
            el_ind++;
        }

        block_ind++;
    }
    let packet = {
        "title" : title,
        "blocks": blocks,
        "published": published,
    };
    console.log(packet);
    return packet;
}

function elelmentBuilder(name, params){
    let el = document.createElement(name);
    for (var key in params){
        el.setAttribute(key, params[key]);
    }
    return el;
}

function titleSpawn(){
    div = elelmentBuilder("div",
    {
        "class": "block",
    });

    title = elelmentBuilder("textarea",
    {
        "class": "h1",
        "rows": 1,
    });
 
    document.querySelector("#content").appendChild(div);
    div.appendChild(title);
}

function paragrapghSpawn(){
    par = elelmentBuilder("textarea",
    {
        "class": "p",
        "rows": 10,  
    });

    div.appendChild(par);
}