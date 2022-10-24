// console.log('hello, javascript');


// function add(num1, num2) {
//     return num1 + num2
// }

// console.log(add(2, 7))


// // 익명함수
// const sub = function (num1, num2) {
//     return num1 - num2
// }

// console.log(sub(2,7))


// const greeting = function (name = 'Anomous') {
//     return `Hi ${name}`
// }

// console.log(greeting())


// // 위의 함수를 화살표 함수로 바꾸기 
// // 1단계_ function 키워드 삭제
// const greeting = (name) => {
//     return `Hi ${name}`
// } 
// //2 단계_ 인자가 1개일 경우에만 () 생략 가능 _ 추천xxx
// const greeting = name => {
//     return `Hi ${name}`
// } 
// // 3단계_ 함수 바디가 return을 포함한 표현식 1개일 경우에 {}와 return 생략 가능
// const greeting = name => `Hi ${name}`


//
// 즉시 실행 함수  
// 함수를 ()로 감싸고 함수의 끝에 (인자)를 추가하여 바로 실행하게 할 수 있음  


//
// 배열 
// 음의 정수 인덱싱 불가능
const numbers = [1, 2, 3, 4, 5]
console.log(numbers[0])
console.log(numbers.length)

// 배열 뒤집기
numbers.reverse()
console.log(numbers)

// 배열에 값 삽입
numbers.push(100)
console.log(numbers)

// 배열의 마지막 값 삭제
numbers.pop()
console.log(numbers)

// 배열에 특정 값이 포함되어있는지 검사
console.log(numbers.includes(1))

// indexOf는 찾으려는 값이 없으면 -1을 반환
console.log(numbers.indexOf(100))

// join
console.log(numbers.join())
console.log(numbers.join('-'))

