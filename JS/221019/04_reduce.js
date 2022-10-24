const numbers = [90, 80, 70, 100]

// 총합. reduce에는 콜백함수와 초기값(0) 총 2개의 인자가 들어감
// function 에도 누적합을 저장할 result와 변수 number 2개의 인자가 들어감
const sumNum = numbers.reduce(function (result, number) {
    return result + number
}, 0)

console.log(sumNum)

// 같은 식
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
