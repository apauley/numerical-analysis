;; This file contains functions and constants that are useful to more
;; than one of the numerical methods.

(define (linear-interpolate f x0 x1)
  "You can imagine this function as drawing a line through two
points that are on a non-linear function f, and returning
the value where the line intersects with the x-axis"
  (- x1
     (* (f x1)
        (/ (- x0 x1)
           (- (f x0) (f x1))))))

(define tolerance 0.00001)
(define (close-enough-to-zero? x)
  (<= (abs x) tolerance))
