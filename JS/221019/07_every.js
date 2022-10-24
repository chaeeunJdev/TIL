// 하나라도 통과하지 못하면 false

const arr = [1,2,3,4,5]

const result = arr.every((elem) => elem % 2 === 0)
console.log(result)