const numbers = [1, 2, 3, 4, 5]


// const doubleEle = function (number) {
//     return number * 2
// }
// const newArry = numbers.map(doubleEle)
// console.log(newArry)

// 같은 식
const newArry = numbers.map((number) => {return number * 2})