#### 직접 정의한 class의 instance를 담은 List에서 max, min 등 비교 연산 수행하고 싶을 때

```java
  /**
  * Comparable<T> 인터페이스를 구현하여 compareTo 메서드를 Overriding 해주면 된다.
  */
  class Document implements Comparable<Document> {
        private int priority;
        private int location;
        
        public Document(int priority, int location) {
            this.priority = priority;
            this.location = location;
        }
        
        public int getPriority() {
            return this.priority;
        }
        
        public int getLocation() {
            return this.location;
        }
        
        @Override
        public int compareTo(Document document) {
            if (this.priority > document.getPriority())
                return 1;
            else if (this.priority < document.getPriority())
                return -1;
            return 0;
        }
```
```java
  import java.util.*;
  import java.util.stream.Collectors;

  Queue<Document> DQ = new LinkedList<>(); //Document를 담는 Queue를 생성하고
  System.out.println(Collections.max(DQ).getPriority()); //DQ에서 가장 큰 우선순위를 갖는 document instance를 찾을 수 있다.
```
