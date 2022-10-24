// const myInfo = {
//     name :'jack',
//     phoneNumber: '123456',
//     'samsung product' : {
//         buds: 'Buds pro',
//         galaxy: 'S99',
//     },
// }

// // .으로 접근
// console.log(myInfo.name)

// // []로 접근
// console.log(myInfo['name'])

// // . []
// console.log(myInfo['samsung product'].galaxy)


// //
// const obj = {
//     name:'jace',
//     greeting() {
//         console.log('hi!')
//     }
// }

// console.log(obj.name)
// console.log(obj.greeting())


// //
// // 계산된 속성값 사용
// const key = 'ssafy'
// const value = ['한국', '미국', '일본', '중국']

// const myObj = {
//     [key]:value,
// }
// console.log(myObj)
// console.log(myObj.ssafy)


// json변환  
const jsonData = {
    coffee : 'Americano',
    iceCream : 'Mint Choco'
}

// Object -> json
const objToJson = JSON.stringify(jsonData)
console.log(objToJson)
console.log(typeof objToJson) // string => json임

// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)
console.log(jsonToObj.coffee) // json을 다시 obj로 바꿨으니 하나의 값에 접근할 수 있음

