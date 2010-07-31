;; Section 1.5 of Applied Numerical Analysis:
;; Fixed-Point Iteration

;; The implementation here is mostly taken from Section 1.3.3 of
;; "Structure and Interpretation of Computer Programs" by Abelson and Sussman


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
