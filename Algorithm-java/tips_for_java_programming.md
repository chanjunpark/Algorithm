***
## List 객체 다루기
#### 직접 정의한 class의 instance를 담은 List에서 instance 변수 이용해 max, min 등 비교 연산 수행하기.
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
***
## Java8 날짜와 시간 다루기(java.time 패키지)
```java
  import java.time.*
```
#### 객체 생성하기
- java.time 패키지에 속한 클래스의 객체 생성은 ```now()```와 ```of()```로 한다.
  - ``` java
    LocalDate localDate = LocalDate.now();
    LocalTime localTime = LocalTime.now();
    ```
  - ``` java
    LocalDate localDate = LocalDate.of(2022, 01, 09);
    LocalTime localTime = LocalTime.of(12, 30, 59);
    ```
#### 두 날짜, 시간 차이 구하기
- Duration(시간 차이), Period(날짜 차이), ChronoUnit(특정 시간 단위로 차이)
- ChronoUnit이 가장 범용성이 높다.
  - ```java
    LocalDateTime startDateTime = LocalDateTime.of(2020, 12, 20, 9, 30, 30); LocalDateTime
    endDateTime = LocalDateTime.of(2022, 12, 20, 10, 0, 40); 
        
    log.debug("Years: {}", ChronoUnit.YEARS.between(startDateTime, endDateTime)); 
    log.debug("Months: {}", ChronoUnit.MONTHS.between(startDateTime, endDateTime)); 
    log.debug("Weeks: {}", ChronoUnit.WEEKS.between(startDateTime, endDateTime)); 
    log.debug("Days: {}", ChronoUnit.DAYS.between(startDateTime, endDateTime)); 
        
    startDateTime = LocalDateTime.of(2022, 12, 20, 9, 30, 30); 
    endDateTime = LocalDateTime.of(2022, 12, 20, 10, 0, 40);
        
    log.debug("Hours: {}",  ChronoUnit.HOURS.between(startDateTime, endDateTime));
    log.debug("Minutes: {}", ChronoUnit.MINUTES.between(startDateTime, endDateTime));
    log.debug("Seconds: {}", ChronoUnit.SECONDS.between(startDateTime, endDateTime));
        
    // Years: 2 
    // Months: 24 
    // Weeks: 104 
    // Days: 730 
    // Hours: 0 
    // Minutes: 30 
    // Seconds: 1810
    // 출처: https://cornswrold.tistory.com/489 [평범한개발자노트]
    ```

 
  


