const avengers = [
    {name: 'Tony', age:45},
    {name: 'Steve', age:32},
    {name: 'Thor', age:40},
]

const avenger = avengers.find((avenger) => {
    return avenger.name === 'Tony'
})

console.log(avenger)
