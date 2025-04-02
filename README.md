# Day-3-of-100
## Treasure Chest Game
Okay I was so excited to do this project because I love story teliing. I love character building and I love adventures. Add in a mix of fantasy elements and interpersonal relationships and I am all in. So taking the course and seeing how the game essentially acts like an otome game or a choose your choice type of game (like ace attorney hehe) I got super excited. 


I'm not gonna lie, I almost flew off the walls with all the ideas that I had, but perhaps it would be more of personal project idea rather than something that I would attempt to do while I'm trying to learn the next 100 days or so. I know..I missed yesterday...it was just a long day. but hey, I call it a win if I came back to this even after taking a break! 

I'm not really sure how to write these READMEs, but I'm starting to get the basics down - that is how to format everything haha! 

I also did a Pizza order calculator for this class and I was also pretty stoked since it was such a real-life application of coding. It made me realize that every industry uses python and coding in general! I've also attached that file to this day! 

## Some things that I have known and reinforced 
- if/else statements. Kind of like: If this condition is fulfuilled then I'll say that, but if not, then something else will happen. 
#### Usage/Examples

```javascript
if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Grow taller to ride the rollercoaster")
```
- Comparator Operators:
  - Greater than (>)
  - Less than (<)
  - Greater than or equal to (>=)
  - Less than or equal to (<=)
  - Equal to (==)
  - Not equal to (!=)
## Some things that I don't remember learning but have a background of:
nothing here, really. 

## Completely New to Me
- Modulos (%)
  - I still have no idea what these are. I'm going to have to do more reading and more video watching on this one. 
  - here's an example of them: 
    - The modulo operator gives you the remainder of a division.
      - 6 % 2 will be 0
      - 6 % 5 will be 1
      - 6 % 4 will be 2
- Nesting
  - I had the hardest trouble with nesting. It is so important, and I keep forgetting how important it is to the code.
  - essentially, you can put if/else statements inside other if/else statements - and these nested ones are noted as "elif"
    ###Usage/Examples

    ```javascript
    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    if height >= 120:
      print("You can ride the rollercoaster")
      age = int(input("what is your age?"))
      if age <= 12:
          print("Please pay $5.")
      elif age <= 18:
          print("Please pay $7")
      #can keep doing elif
      else:
          print("Please pay $12")
    else:
      print("Sorry you have to grow taller before you can ride.")
    ```
  - There are also multiple types of IF statements too. Especially if there are different conditions that are not totally unrelated to each other.
    ```javascript
    # If/elif/else
    if <condition 1 is true>
      <do A>
    elif <condition 2 is true>
      <do B>
    else
        <do C>
    # Nested if statements
    if <condition 1 is true>
        <do A>
        if <condition 2 is true>
            <do B>
            if <condition 3 is true>
                <do C>
    # Multiple if statements
    if <condition 1 is true>
        <do A>
    if <condition 2 is true>
        <do B>
    if <condition 3 is true>
        <do C>
    ```
  - Logical Operators
      ```javascript
      A and B #Both conditions need to be true
      C or D #Only one condition needs to be true
      not E #The condition must be false

      example:
        elif  45 <= age <=  55: #less words of codes no "and" however it is harder to read
          print("Your tickets are free because you are going through a mid-life crisis")
      OR
        elif age>=45 and age<=55
      ```
    
