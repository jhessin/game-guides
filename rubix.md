# Solving a Rubix Cube

## Step 1 - Make a daisy

Pretty self explanatory. No real tricks just Park your white cars around your
yellow house... ;)

## Step 2 - Make a white plus

With the yellow side on the top rotate the top until the tip of your daisy
pieces matches the center color of your front facing piece and then flip the
front face.

## Step 3 - Solve the white side

The parable of the farmers and the lost dogs.

## Step 4 - Solve the 2nd layer

Remember the Yellow side is facing you for this part.
The focus piece is top side piece and it should have no yellow.
Align the color of the focus piece with it's color on top making a 'T'

### ABC's
```
Away
Bottom
Columns come down
Delicious Sandwich
Everything Goes Back Up
Find/Fix your whites
```

The color facing you on your focus piece determines your keyword (right/left)
The abc's refer to your keyword.

Turn the Front face away from your keyword
Move the Bottom toward your keyword
Column comes down on keyword side
Turn the meat of your delicious sandwich toward your keyword.
Everything goes back up on your keyword side.
Fixing the whites is always a simple step.

## Step 5 - Make a yellow plus

Yellow is on TOP for this step.


### Positioning the cube

Before doing those moves check for the boomerang (point it to the left and up)
or the line (point it to the left and right).

As long as you have those guides just keep doing the FUR-URF and eventually you
will get the yellow plus.

NOTE: THE SIDE/CORNER COLORS DO NOT MATTER! As long as you have a yellow plus
your can move on to the next step.

### Algorithm
```
FUR-URF

# Clockwise moves
- Front
- Up
- Right

# Counterclockwise moves
- Up
- Right
- Front
```

## Step 6 - Solve yellow side ( FACE ONLY! )

ALL movement patterns start on the right side.

There are 4 possible starting patterns:

Legend: * (yellow) - (other)

Clean Plus:
```
-*-
***
-*-
```

There should be 2 yellow corners. You should face the cube so these corners are
on your left.

Fish:
```
-*-
***
**-
```

This needs to face down and toward the left.

Turtle:
```
***
***
-*-
```

Make sure the turtle is facing you.

Crab:
```
**-
***
-**
```

The crab should have his 'food' (a yellow piece) facing you and on the left
while the crab is facing the bottom left.

The algorithm should be done alternating on the right and top sides with yellow
on the top.

### Algorithm
```
Clock, Clock, Counter,
Clock, Clock, Flip, Counter
```

Reposition and repeat as many times as necessary.

## Step 7 - Solve the yellow corners ( NOT sides )

Yellow is on the top.

Find to matching corner pieces and spin the top until they are on their
appropriate side. If all the sides have appropriate corners you are done and can
move on to the next step - otherwise place the most completed side away from
you.

Hold the cube on the left and rotate the sides in this order:

Right - Front - Right - Back 

### Algorithm
```
Counter
Clock
Counter
Flip
Clock
Counter
Counter
Flip
Flip
```

NOTE: Ignore the sides for this step - if all the corners are right move on to
the next step.

## Step 8 - Solve the CUBE!

Yelllow is on top.
Perform the algorithm on these sides
Right - Top 

May require multiple times.

### Algorithm
```
Flip
3 Clocks
5 Counters
Clock
Counter
```
