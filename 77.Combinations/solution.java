public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (k>n) { return res; }
        List<Integer> state = new ArrayList<>(k);
        for (int i=1; i<=k; i++) { state.add(i); }
        boolean done = false;
        while (!done) {
            res.add(new ArrayList(state));
            done = true;
            for (int pos=k-1;pos>=0; pos--) {
                if (state.get(pos) < n-(k-1-pos)) {
                    state.set(pos,state.get(pos)+1);
                    int cur = state.get(pos);
                    for (int b=pos+1; b<k;b++) {
                        state.set(b,cur +1);
                        cur = state.get(b);
                    }
                    done = false;
                    break;
                }
            }
        }
        return res;
    }
}
