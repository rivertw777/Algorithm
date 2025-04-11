import java.util.*;

class Solution {
    public int solution(int bl, int w, int[] tw) {
        List<int[]> bridge = new ArrayList<>();
        List<Integer> truckWeights = new ArrayList<>();
        
        // 트럭 무게 배열을 리스트로 변환
        for (int weight : tw) {
            truckWeights.add(weight);
        }
        
        int time = 0;
        while (true) {
            // 지나간 트럭 삭제
            if (!bridge.isEmpty() && bridge.get(0)[1] == bl) {
                bridge.remove(0);
            }
            
            // 트럭 삽입
            if (!truckWeights.isEmpty() && bridge.isEmpty()) {
                bridge.add(new int[]{truckWeights.get(0), 0});
                truckWeights.remove(0);
            }
            // 다리 길이 체크
            else if (!truckWeights.isEmpty() && bridge.size() <= bl) {
                int total = 0;
                for (int[] truck : bridge) {
                    total += truck[0];
                }
                
                // 무게 체크
                if (total + truckWeights.get(0) <= w) {
                    bridge.add(new int[]{truckWeights.get(0), 0});
                    truckWeights.remove(0);
                }
            }
            
            // 시간 경과
            time++;
            for (int[] truck : bridge) {
                truck[1]++;
            }
            
            // 종료 조건
            if (truckWeights.isEmpty() && bridge.isEmpty()) {
                break;
            }
        }
        
        return time;
    }
}