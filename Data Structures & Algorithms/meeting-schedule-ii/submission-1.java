/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        intervals.sort(Comparator.comparing(intv->intv.start));

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int rooms = 0;
        int n = intervals.size();

        for(int i =0; i<n ; i++){
            var intv = intervals.get(i);
            int start = intv.start;
            int end = intv.end;
            if(!pq.isEmpty() && pq.peek()<=start){
                pq.poll();
            }
            else{
                rooms += 1;
            }
            pq.offer(end);
        }
        return rooms;
    }
}
