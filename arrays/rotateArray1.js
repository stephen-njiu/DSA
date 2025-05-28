const reverse = function(nums, start, end) {
    while (start < end){
        [nums[start], nums[end]] = [nums[end], nums[start]]
        start ++
        end --
    }

}

const rotate = function(nums, k) {
    k = k%nums.length
    reverse(nums, 0, nums.length -1)
    reverse(nums, 0, k-1)
    reverse(nums, k, nums.length-1)
    return nums
}

k = 22
a = [3,44,3,5,2]
b = []
c = [3, 2, 4, 6, 1, 7, 8, 83]

console.log(rotate(c,k))