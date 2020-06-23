$(document).ready(function(){

    $(".article-save").on("click",(e)=>{
        let elem = e.target
        let id = elem.getAttribute("article-id")
        fetch("http://localhost:8000/rss/save/?id=" + id);

    })

    $(".article-delete").on("click",(e)=>{
        let elem = e.target
        let id = elem.getAttribute("article-id")
        fetch("http://localhost:8000/rss/delete/?id=" + id);

    })


      var elems = document.querySelectorAll('#autocomplete-input');
      var instance = M.Autocomplete.init(elems, {})[0];
      elems[0].oninput = async function(e) {
        let text = e.target.value;
        if(text.length == 2){
            console.log("http://localhost:8000/rss/tags/?tags=" + text);
            fetch("http://localhost:8000/rss/tags/?tags=" + text).
            then(response => response.json()).
            then(json_tags => {
                instance.updateData(json_tags)

            })
        }
      };


  });

