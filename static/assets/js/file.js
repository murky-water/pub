
document.addEventListener("click",function dismissMenu(e){
    document.getElementById("search_ul").classList.add("d-none");
})
function drawSearchResult(arr){
        const parser = new DOMParser();
    const ul = document.getElementById("search_ul");
    ul.textContent='';
    for (const i of arr) {
	const str = '<li class="mb-1">					           <img src="'+i.image+'" class="me-2" width=50px height=50px>                                  <div class="fs-5 align-items-center">                    '+i.name+'                  </div>                </li>';	
	const doc = parser.parseFromString(str, 'text/html');
			const el = doc.body.firstChild;
	ul.appendChild(el);
	
    }
}
function showMenu(e) {
    document.getElementById("search_ul").classList.remove("d-none");
      e.stopPropagation();
}
document.getElementById("location").addEventListener ("input", searchData);
async function searchData(e) {
    showMenu(e)
    type=e.target.id;
    keyword=e.target.value;
  const url = "search?type="+type+"&keyword="+keyword;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const data = await response.json();
    
      drawSearchResult(JSON.parse(data));
  } catch (error) {
    console.error(error.message);
  }
}
