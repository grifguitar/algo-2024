- [визуализация дерева (search_tree.py)](https://github.com/grifguitar/algo-2024/blob/main/examples/search_tree/search_tree.py)
  и [пример запроса k-го элемента (search_tree_kth.py)](https://github.com/grifguitar/algo-2024/blob/main/examples/search_tree/search_tree_kth.py)
  ```
                           (10,2314)
     (2,4950)                          (55,7823)
  (,)           (3,8334)            (,)         (,)
             (,)        (,)
  ```
  вершины описаны в формате `(key, priority)`

- [визуализация дерева по неявному ключу (search_tree_x_impicit.py)](https://github.com/grifguitar/algo-2024/blob/main/examples/search_tree/search_tree_x_impicit.py)
  для массива `arr = [5, 4, 3, 2, 1]`
  ```
               (4,0,15)
     (5,0,5)                                  (1,0,6)
  (,)       (,)                     (2,0,5)          (,)
                          (3,0,3)          (,)
                       (,)       (,)
  ```
  после запроса массового обновления на полуинтервале `arr[0..5] += 10`:
  ```
                (14,0,65)
     (5,10,5)                                   (1,10,6)
  (,)        (,)                      (2,0,5)           (,)
                            (3,0,3)          (,)
                         (,)       (,)
  ```
  вершины описаны в формате `(data, flag, sum)`