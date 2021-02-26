//PF-Exer-16

num1=5
num2=10

//Write your code here
if(num2>num1){
    i = num2
    while(i%num1!=0){
        i+=num2
    }
}
else {
    i=num1
    while(i%num2!=0){
        i+=num1
    }
}
console.log(i)
