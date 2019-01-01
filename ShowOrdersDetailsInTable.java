
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

public class ShowOrdersDetailsInTable {
	public static void main(String[] args) throws Exception {
		JSONObject outPutJson = new JSONObject(); 
		try {
			 if (args.length != 1)
				 throw new Exception("You need to pass one argument");
			outPutJson = new JSONObject("{ \"hadError\": \"false\", \"error\": \"\"}");
			JSONObject json = new JSONObject(args[0]);

			JSONArray jsonArr = json.getJSONArray("orders");
			JTable table = new JTable();
			DefaultTableModel dataForTable;
			JFrame frame = new JFrame("orders");
			JScrollPane scrollPane = new JScrollPane(table);
			String[] columnNames = { "Orders ID", "Customer Name", "Customer Phone","Date", "products" };
			dataForTable = new DefaultTableModel(columnNames, 0);
			table.setModel(dataForTable);
			// Insert products into the table.
			for (int i = 0; i < jsonArr.length(); i++) {
				String prods="";
				JSONObject order = jsonArr.getJSONObject(i);
				JSONArray JprodNames=order.getJSONArray("productsNames");
			
				for (int j = 0; j < JprodNames.length(); j++) {
					prods+=JprodNames.getString(j);
					if(j+1<JprodNames.length())
						prods+=", ";
				}
				Object orderRecord[] = { order.getInt("ordID"), order.getString("custName"),
						order.getString("custPhone"),order.getString("ordDate"),prods};				
				dataForTable.addRow(orderRecord);
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
		}
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
