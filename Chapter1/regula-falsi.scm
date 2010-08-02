;; The Method of False Position (Regula Falsi)
;; Section 1.2, p. 40 of Applied Numerical Analysis

;; This method is similar to the secant method, except that
;; (f x0) and (f x1) need to bracket the root (have opposite signs),
;; like the bisection method.

(load "helpers")
(define (regula-falsi f x0 x1)
  (define x2 (linear-interpolate f x0 x1))
  (define (opposite-sign? value1 value2)
    (<= (* value1 value2) 0))

  (println x0 " " x1 " " x2 " " (f x2))
  (if (close-enough-to-zero? (f x2))
      x2
      (if (opposite-sign? (f x2) (f x0))
          (regula-falsi f x0 x2)
          (regula-falsi f x2 x1))))

(println (regula-falsi example-f 0 1))
