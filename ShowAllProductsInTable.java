import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import java.awt.BorderLayout;
import org.json.JSONArray;
import org.json.JSONObject;

public class ShowAllProductsInTable {
	  public static void main(String[] args) throws Exception {
		//String structureOfJson = { products: [] };
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			
			//String test = "{ 'products' : [{ 'prodID' : 3, 'prodName' : 'table', 'price' : 50}, { 'prodID' : 2, 'prodName' : 'bag', 'price' : 100}]}";
			JSONObject json = new JSONObject(args[0]);
			JTable table = new JTable();
			DefaultTableModel data;
			JFrame frame = new JFrame();
			JScrollPane scrollPane = new JScrollPane(table);
			String[] columnNames = {"Productd ID", "Productd Name", "Price"};
			data = new DefaultTableModel(columnNames,0);
			table.setModel(data);
			
			JSONArray jsonArr = json.getJSONArray("products");
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject product = jsonArr.getJSONObject(i);
				Object newData[] = {product.getInt("prodID"), product.getString("prodName"), product.getInt("price")};
				data.addRow(newData);
				}
			// Show all products in table.
		    frame.add(scrollPane, BorderLayout.CENTER);
		    frame.setSize(300, 150);
		    frame.setVisible(true);
		}
		catch(Exception err) {
			System.out.println(err);
		}
		//finally:
		//	System.out.println(structureOfJson);
}
}