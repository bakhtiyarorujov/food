window.addEventListener('load', async function(event){
    let responseCategory = await this.fetch("http://localhost:8000/api/categories")
    let resDataCategory = await responseCategory.json()
    let categorySelect = this.document.querySelector("[name='category']")
    for (category of resDataCategory){
        categorySelect.innerHTML += `
        <option value="${category.id}">${category.name}</option>
        `
    }
    let responseTags = await this.fetch("http://localhost:8000/api/tags")
    let resDataTag = await responseTags.json()
    let tagSelect = this.document.querySelector("#tag-select")
    for (tag of resDataTag){
        tagSelect.innerHTML += `
        <option value="${tag.id}">${tag.name}</option>
        `
    }
})

let recipeCreateForm = document.querySelector('#recipeForm')
recipeCreateForm.addEventListener('submit', function(event){
    event.preventDefault()
    let formData = new FormData(recipeCreateForm)
    let response = fetch("http://localhost:8000/api/recipes", {
        method: "POST",
        headers: {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwMTEyMjM3LCJpYXQiOjE3MjAwMjU4MzcsImp0aSI6IjJkNmFkOTNmOGNhMjQ4MTBiMmJiYjBkZTlkMmVmN2QwIiwidXNlcl9pZCI6MX0.Dm_rffkrNBlrgufOpLDc6FDebjwnkpK9IsaO3MSovNw'
        },
        body: formData
    })

})