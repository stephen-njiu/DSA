function sortedSquaredArray(array) {
    const newArray = new Array(array.length).fill(0)
    let pointerLeft = 0;
    let pointerRight = array.length -1
    for (let i = array.length-1; i>=0;i--){
        const leftSquared = Math.pow(array[pointerLeft],2)
        const rightSquared = Math.pow(array[pointerRight],2)
        if (leftSquared > rightSquared) {
            newArray[i] = leftSquared
            pointerLeft ++ 
        } else {
            newArray[i] = rightSquared
            pointerRight --
        }
    }
    return newArray
}

a = [-3,-3,7,13, 18]
b = [1, 4, 5, 7]
c = [-11, 1, 4, 5, 9]

console.log(sortedSquaredArray(a))
console.log(sortedSquaredArray(b))
console.log(sortedSquaredArray(c))