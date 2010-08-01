;; Section 1.5 of Applied Numerical Analysis:
;; Fixed-Point Iteration, p. 54

;; The implementation here is mostly taken from the MIT textbook
;; "Structure and Interpretation of Computer Programs" by Abelson and
;; Sussman (Section 1.3.3)
;; http://mitpress.mit.edu/sicp/full-text/book/book.html
;; http://en.wikipedia.org/wiki/Structure_and_Interpretation_of_Computer_Programs

;; The fixed-point function takes as arguments a function f
;; and a number to be used as the initial guess.
;; It then calls itself recursively until it arrives at a
;; fixed-point of f.

(define (fixed-point f initial-guess)
  (define next-guess (f initial-guess))
  (define tolerance 0.00001)
  (define (close-enough? value1 value2)
    (<= (abs (- value1 value2)) tolerance))

  (println initial-guess)
  (if (close-enough? initial-guess next-guess)
      next-guess
      (fixed-point f next-guess)))

(define (fx x)
  (- (* x x) (* 2 x) 3))

(define (g1 x)
  (sqrt (+ (* 2 x) 3)))

(define (g2 x)
  (/ 3 (- x 2)))

(fixed-point g2 4.0)
