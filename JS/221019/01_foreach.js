// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
    console.log(color)
}

colors.forEach(printClr)

// 2.
colors.forEach(function (color) {
    console.log(color)
})

// 3. 1번식을 이렇게 표현할 수 있어야 함
colors.forEach((color) => console.log(color))