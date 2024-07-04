window.addEventListener('load', async function(event){
    let response = await this.fetch('http://localhost:8000/api/recipes')
    let resData = await response.json()
    let recipe_list = document.querySelector("#recipe_list")
    for (recipe of resData){
        recipe_list.innerHTML += `
        <div class="card" style="width: 18rem;">
            <img src="${recipe.cover}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${recipe.title} - ${recipe.category.name}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        `
    }
})