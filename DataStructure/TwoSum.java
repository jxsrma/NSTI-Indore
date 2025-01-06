import java.util.*;

class TwoSum {
    public static void main(String[] args) {
        int arr[] = { 2, 6, 7, 5, 3 };
        int sum = 13;

        Set<Integer> s = new HashSet<>();

        for (int i = 0; i < arr.length; i++) {
            s.add(arr[i]);
        }
        for (int i = 0; i < arr.length; i++) {
            if (s.contains(sum - arr[i])) {
                System.err.println(sum - arr[i] + "," + arr[i]);
                break;
            }
        }

    }
}