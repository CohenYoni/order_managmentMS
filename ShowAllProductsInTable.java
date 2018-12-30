import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.JTableHeader;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import org.json.JSONArray;
import org.json.JSONObject;

public class ShowAllProductsInTable {
	public static void main(String[] args) throws Exception {
		JSONObject outPutJson = new JSONObject(); 
		try {
			 if (args.length != 1)
				 throw new Exception("You need to pass one argument");
			outPutJson = new JSONObject("{ \"hadError\": \"true or false\", \"error\": \"some details of the error\"}");
			//String test = "{ 'products' : [{ 'prodID' : 3, 'prodName' : 'table', 'price' : 50}, { 'prodID' : 2, 'prodName' : 'bag', 'price' : 100}]}";
			JSONObject json = new JSONObject(args[0]);
			JSONArray jsonArr = json.getJSONArray("products");
			JTable table = new JTable();
			DefaultTableModel dataForTable;
			JFrame frame = new JFrame("Products");
			JScrollPane scrollPane = new JScrollPane(table);
			String[] columnNames = { "Productd ID", "Productd Name", "Price" };
			dataForTable = new DefaultTableModel(columnNames, 0);
			table.setModel(dataForTable);
			
			// Insert products into the table.
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject product = jsonArr.getJSONObject(i);
				Object productRecord[] = { product.getInt("prodID"), product.getString("prodName"),
						product.getInt("price") };
				dataForTable.addRow(productRecord);
			}
			// Design table head.
			JTableHeader Theader = table.getTableHeader();
			Theader.setBackground(Color.GRAY);
			Theader.setFont(new Font("Ariel", Font.PLAIN, 16));
			
			// Design table rows.
			table.setFont(new Font("Ariel", Font.PLAIN, 15));
			table.setRowHeight(20);
			
			// Show all products in table.
			frame.add(scrollPane, BorderLayout.CENTER);
			frame.setSize(400, 200);
			frame.setVisible(true);
		catch(Throwable err) {
			outPutJson = new JSONObject();
			outPutJson.put("hadError", true);
			outPutJson.put("error", err);
		}
		finally
		{
			System.out.println(outPutJson.toString());
		}
	}
}