;; The Secant Method
;; Section 1.2, p. 38 of Applied Numerical Analysis

;; secant takes as input a function f and 2 initial values (x0 and x1),
;; from which a third value is computed.
;; The function then calls itself recursively with newly computed values,
;; until a root of f is found.

(define (secant f x0 x1)
  (define x2
    (- x1
       (* (f x1)
          (/ (- x0 x1)
             (- (f x0) (f x1))))))

  (define (close-enough? x)
    (= (abs x) 0))

  (println x0 " " x1 " " x2 " " (f x2))
  (if (close-enough? (f x2))
      x2
      (secant f x1 x2)))

(define (fx x)
  (+ (* 3 x) (sin x) (- (exp x))))

(println (secant fx 1 0))
