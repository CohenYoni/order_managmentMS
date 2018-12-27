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
		String[] prodArr = strs.toArray(new String[strs.size()]);
		JFrame frame = new JFrame("all products");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JList<String> products = new JList<String>(prodArr);
		JScrollPane scrollPane = new JScrollPane(products);
		frame.add(scrollPane, BorderLayout.CENTER);
	    frame.setSize(300, 150);
	    frame.setVisible(true);
	}
}
