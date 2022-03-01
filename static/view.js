function clipboard(domObject) {
    domObject.parentNode.parentNode.childNodes.
        forEach(
        (x) => {
            if (x.className == "routes")
            {
                console.log(x.href)
                navigator.clipboard.writeText(x.href);
            }
        }
    );
} 