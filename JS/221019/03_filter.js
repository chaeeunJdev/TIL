const products = [
    {name: 'cucumber', type:'vegetable'},
    {name : 'banana', type:'fruit'},
    {name : 'carrot', type:'vegetable'},
    {name : 'apple', type:'fruit'},

]

// const fruitFilter = function (product) {
//     return product.type === 'fruit'
// }

// const newArry = products.filter(fruitFilter)
// console.log(newArry)

// // 같은 식
const newArry = products.filter((product) => {
    return product.type === 'fruit'
})