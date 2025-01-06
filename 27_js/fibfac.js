//Team TopherAcademy1 :: Mark Ma, Anastasia Lee
//SoftDev pd4
//K27 - Basic functions in JavaScript
//2025-01-06m

//JavaScript implementations of Day0 recursive Scheme functions

//factorial:

//<your team's fact(n) implementation>

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

function fact(n){
  if (n == 1){
    return 1;
  }
  return fact(n - 1) * n;
}

console.log(fact(5))
console.log(fact(6))
//-----------------------------------------------------------------


//fib:

//<your team's fib(n) implementation>

function fib(n){
  if(n < 2){
    return n;
  }
  return fib(n-1) + fib(n-2);
}

//TEST CALLS
// (writing here can facilitate EZer copy/pasting into dev console now and later...)

console.log(fib(3))
console.log(fib(4))

//=================================================================

