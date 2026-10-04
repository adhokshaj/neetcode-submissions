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
    public boolean canAttendMeetings(List<Interval> intervals) {
        intervals.sort(Comparator.comparing(intv->intv.start));

        int n = intervals.size();
        for (int i =0; i<n-1; i++){
            var int1 = intervals.get(i);
            var int2 = intervals.get(i+1);

            if(int2.start<int1.end){
                return false;
            }
        }
        return true;
    }
}
