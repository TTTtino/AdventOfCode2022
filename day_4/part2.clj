(require '[clojure.string :as string])
(require '[clojure.set :as set])

(defn create-sets [nums]
  (let [a (range (nth nums 0) (+ (nth nums 1) 1))
        b (range (nth nums 2) (+ (nth nums 3) 1))]

    (->> (list a b)
         (map set))))

(defn test-any-overlap [sets]
  (not (empty? (set/intersection (nth sets 0) (nth sets 1)))))


(defn get-sets-from-str [line] (->> (re-find #"(\d+)-(\d+),(\d+)-(\d+)" line)
                                    (drop 1)
                                    (map parse-long)
                                    (create-sets)))

(defn get-num-any-overlap [file]
  (->> (slurp file)
       (string/split-lines)
       (map get-sets-from-str)
       (map test-any-overlap)
       (filter #(= true %))
       (count)
       (println)))

(defn main []
  (get-num-any-overlap "input.txt"))


(main)
