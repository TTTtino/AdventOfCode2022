(require '[clojure.string :as string])
(require '[clojure.set :as set])

(defn create-sets [nums]
  (let [a (range (nth nums 0) (+ (nth nums 1) 1))
        b (range (nth nums 2) (+ (nth nums 3) 1))]

    (->> (list a b)
         (map set))))

(defn test-complete-overlap [sets]
  (or (set/subset? (nth sets 0) (nth sets 1)) (set/subset? (nth sets 1) (nth sets 0))))

(defn test-overlap-str [line] (->> (re-find #"(\d+)-(\d+),(\d+)-(\d+)" line)
                                   (drop 1)
                                   (map parse-long)
                                   (create-sets)
                                   test-complete-overlap))
(defn get-num-complete-overlap [file]
  (->> (slurp file)
       (string/split-lines)
       (map test-overlap-str)
       (filter #(= true %))
       (count)
       (println)))

(defn main []
  (get-num-complete-overlap "input.txt"))



(main)