import java.awt.BorderLayout;
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JScrollPane;

public class MessageBox {
	static public void main(String[] args) {
		ArrayList<String> strs = new ArrayList<String>();
		for (int i = 0; i < 50; i++)
			strs.add(Integer.toString(i));
		String[] strArr = strs.toArray(new String[strs.size()]);
		JFrame frame = new JFrame("title");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JList<String> jListStr = new JList<String>(strArr);
		JScrollPane scrollPane = new JScrollPane(jListStr);
		frame.add(scrollPane, BorderLayout.CENTER);
	    frame.setSize(200, 200);
	    frame.setVisible(true);
	}
}
