/* helps get link node of the route map object polling from the
   parent node tree from the buttons being used*/
function getRouteMapA(node){
    var result;
    node.parentNode.parentNode.childNodes.
        forEach(
        (x) => {
            if (x.className == "routes")
            {
                result = x;
            }
        }
    );
    if (result){
        return result;
    }
}

/* copy button gets shortened route to clipboard */
function clipboard(domObject) {
    var node = getRouteMapA(domObject);
    navigator.clipboard.writeText(node.href);
}

/* removes the route from DOM and the database */
function remove(domObject) {
    var node = getRouteMapA(domObject);

    /* sends the request to server to delete from DB */
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            /* removes whole route object from DOM */
            node.parentNode.remove();
        }
    };
    console.log("sending delete request");
    console.log(node)
    xhttp.open("POST", "/remove/route/" + node.attributes["dbid"].nodeValue, true);
    xhttp.send();
}