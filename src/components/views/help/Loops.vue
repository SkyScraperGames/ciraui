<template>
  <div class="container content">
    <h1>Python - Loops</h1>

    <p>
      Loops are fairly similar to conditional statements. Like conditionals, loops execute code when a condition evaluates to true.
      The difference is that loops will execute that code over and over again as long as that condition is still true. An example
      of a loop in real life might be:
    </p>

    <p style="text-align: center;">
      <em>I will keep rolling these dice as long as one of them is less than 3</em>
    </p>
    <p>
      This person is saying that they will roll the dice over and over again as long as one of the dice is less than 3. In Python,
      this might look like:
    </p>

    <pre style="text-align: left;"><code>while dice1 &lt; 3 or dice2 &lt; 3:
      rolldice()
    </code></pre>

    <p>
      This is what a loop looks like in Python. Specifically, it is what we call a
      <strong>while</strong> loop. While loops are loops that will keep executing
      <strong>while</strong> their condition is true. This means that it is possible for a while loop to never stop. This is called
      an infinite loop, and it is something that you want to avoid. Thankfully, there is another type of loop that can prevent
      this problem. This type of loop is called a
      <strong>for</strong> loop. It works by having its condition say the number of times it is going to execute its code. For example:</p>
    <p></p>

    <pre style="text-align: left;"><code>for x in range(10, 20):
    print x
    </code></pre>

    <p>This code tells the computer to go from 10 to 20 (but stop before 20) and print each number.</p>
  </div>
</template>
