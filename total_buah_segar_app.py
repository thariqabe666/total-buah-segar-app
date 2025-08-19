
import streamlit as st
import pandas as pd

# Initialize session state for cart and fruit list
if 'daftar_buah' not in st.session_state:
    st.session_state.daftar_buah = [
        {'Nama': 'Apel', 'Stock': 20, 'Harga': 10000},
        {'Nama': 'Jeruk', 'Stock': 10, 'Harga': 15000},
        {'Nama': 'Anggur', 'Stock': 25, 'Harga': 20000}
    ]
if 'keranjang' not in st.session_state:
    st.session_state.keranjang = []

def format_rupiah(harga):
    """Format number to Rupiah currency string."""
    return f"Rp{harga:,.0f}".replace(',', '.')

def calculate_total(keranjang):
    """Calculate total price of items in the cart."""
    return sum(item['Jumlah'] * item['Harga'] for item in keranjang)

def main():
    st.set_page_config(page_title="Ultra Buah Segar", layout="wide")
    st.title("🍓 Ultra Buah Segar Market")

    # Sidebar for actions
    menu = ["Tampilkan Buah", "Tambah Buah", "Hapus Buah", "Keranjang"]
    pilihan = st.sidebar.selectbox("Pilih Menu", menu)

    if pilihan == "Tampilkan Buah":
        st.header("Daftar Buah Tersedia")
        if not st.session_state.daftar_buah:
            st.warning("Tidak ada buah yang tersedia saat ini.")
        else:
            df = pd.DataFrame(st.session_state.daftar_buah)
            df['Harga'] = df['Harga'].apply(format_rupiah)
            st.dataframe(df, use_container_width=True)

            st.subheader("Beli Buah")
            if not st.session_state.daftar_buah:
                st.info("Silakan tambah buah terlebih dahulu.")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    selected_fruit_name = st.selectbox("Pilih Buah", [buah['Nama'] for buah in st.session_state.daftar_buah])
                
                selected_fruit = next((item for item in st.session_state.daftar_buah if item["Nama"] == selected_fruit_name), None)

                if selected_fruit:
                    with col2:
                        jumlah_beli = st.number_input("Jumlah", min_value=1, max_value=selected_fruit['Stock'], step=1)
                    
                    if st.button("Tambahkan ke Keranjang"):
                        item_in_cart = next((item for item in st.session_state.keranjang if item["Nama"] == selected_fruit_name), None)
                        if item_in_cart:
                            item_in_cart['Jumlah'] += jumlah_beli
                        else:
                            st.session_state.keranjang.append({
                                'Nama': selected_fruit_name,
                                'Jumlah': jumlah_beli,
                                'Harga': selected_fruit['Harga']
                            })
                        selected_fruit['Stock'] -= jumlah_beli
                        st.success(f"{jumlah_beli} {selected_fruit_name} telah ditambahkan ke keranjang!")
                        st.rerun()

    elif pilihan == "Tambah Buah":
        st.header("Tambah Buah Baru")
        with st.form("tambah_buah_form"):
            nama_baru = st.text_input("Nama Buah")
            stock_baru = st.number_input("Stock", min_value=0, step=1)
            harga_baru = st.number_input("Harga", min_value=0, step=1000)
            submitted = st.form_submit_button("Tambah")

            if submitted:
                if any(buah['Nama'].lower() == nama_baru.lower() for buah in st.session_state.daftar_buah):
                    st.error(f"Buah '{nama_baru}' sudah ada.")
                elif not nama_baru:
                     st.error("Nama buah tidak boleh kosong.")
                else:
                    st.session_state.daftar_buah.append({'Nama': nama_baru, 'Stock': stock_baru, 'Harga': harga_baru})
                    st.success(f"Buah '{nama_baru}' berhasil ditambahkan!")

    elif pilihan == "Hapus Buah":
        st.header("Hapus Buah")
        if not st.session_state.daftar_buah:
            st.warning("Tidak ada buah untuk dihapus.")
        else:
            nama_hapus = st.selectbox("Pilih Buah untuk Dihapus", [buah['Nama'] for buah in st.session_state.daftar_buah])
            if st.button("Hapus"):
                st.session_state.daftar_buah = [buah for buah in st.session_state.daftar_buah if buah['Nama'] != nama_hapus]
                st.success(f"Buah '{nama_hapus}' telah dihapus.")
                st.rerun()

    elif pilihan == "Keranjang":
        st.header("Keranjang Belanja Anda")
        if not st.session_state.keranjang:
            st.info("Keranjang Anda kosong.")
        else:
            keranjang_df = pd.DataFrame(st.session_state.keranjang)
            keranjang_df['Total'] = keranjang_df['Jumlah'] * keranjang_df['Harga']
            
            # Display cart items
            st.dataframe(keranjang_df[['Nama', 'Jumlah', 'Harga', 'Total']].set_index('Nama'), use_container_width=True)

            # Display total
            total_belanja = calculate_total(st.session_state.keranjang)
            st.markdown(f"### Total Belanja: {format_rupiah(total_belanja)}")

            col1, col2 = st.columns([1,1])
            with col1:
                if st.button("Checkout", use_container_width=True):
                    st.session_state.keranjang = []
                    st.success("Terima kasih telah berbelanja!")
                    st.rerun()
            with col2:
                if st.button("Kosongkan Keranjang", use_container_width=True):
                    # Logic to return stock is not included for simplicity
                    st.session_state.keranjang = []
                    st.info("Keranjang telah dikosongkan.")
                    st.rerun()

if __name__ == "__main__":
    main()
